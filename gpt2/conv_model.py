from transformers.models.rag.retrieval_rag import requires_backends
from transformers import T5Tokenizer, AutoModelForCausalLM

# トークナイザーとモデルの準備
tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
model = AutoModelForCausalLM.from_pretrained("./gpt2/output/")

def generate_reply(message: str) -> str:
    message_input = "<s>" + message +"[SEP]"
    tokenized = tokenizer.encode(message_input, return_tensors="pt")
    output = model.generate(tokenized, do_sample=True, max_length=60, num_return_sequences=8, 
                            top_p=0.95, top_k=20, bad_words_ids=[[1], [5]], no_repeat_ngram_size=3)
    output_list = tokenizer.batch_decode(output)
    for i in range(3):
        response = output_list[i]
        response = response.split('[SEP] </s>')[1]
        response = response.replace('</s>', '')
        if '<unk>' in response or '(' in response or ')' in response:
            continue
        end = response.rfind('。')
        if end == -1:
            continue
        response = response[:(end+1)]
        break

    return response
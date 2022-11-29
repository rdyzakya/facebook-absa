# T5 family
from transformers import T5ForConditionalGeneration, T5TokenizerFast, ByT5Tokenizer, MT5ForConditionalGeneration

# XGLM
from transformers import XGLMTokenizerFast, XGLMForCausalLM

# BART
from transformers import BartForConditionalGeneration, BartTokenizerFast, MBartForConditionalGeneration, MBartTokenizerFast

# GPT
from transformers import GPT2TokenizerFast, GPT2LMHeadModel


# https://huggingface.co/models?pipeline_tag=text2text-generation&sort=downloads&search=indo
# https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads&search=indo

# https://huggingface.co/docs/transformers/model_summary#seq-to-seq-models
# https://huggingface.co/docs/transformers/model_summary#autoregressive-models
def get_gabsa_tokenizer_and_model(model_type,model_name_or_path,model_args,tokenizer_args):
    tokenizer = None
    model = None
    if model_type == "t5":
        model = T5ForConditionalGeneration.from_pretrained(model_name_or_path,**model_args)
        tokenizer = T5TokenizerFast.from_pretrained(model_name_or_path,**tokenizer_args)
    elif model_type == "byt5":
        model = T5ForConditionalGeneration.from_pretrained(model_name_or_path,**model_args)
        tokenizer = ByT5Tokenizer.from_pretrained(model_name_or_path,**tokenizer_args)
    elif model_type == "mt5":
        model = MT5ForConditionalGeneration.from_pretrained(model_name_or_path,**model_args)
        tokenizer = T5TokenizerFast.from_pretrained(model_name_or_path,**tokenizer_args)
    elif model_type == "xglm":
        model = XGLMForCausalLM.from_pretrained(model_name_or_path,**model_args)
        tokenizer = XGLMTokenizerFast.from_pretrained(model_name_or_path,**tokenizer_args)
    elif model_type == "bart":
        model = BartForConditionalGeneration.from_pretrained(model_name_or_path,**model_args)
        tokenizer = BartTokenizerFast.from_pretrained(model_name_or_path,**tokenizer_args)
    elif model_type == "mbart":
        model = MBartForConditionalGeneration.from_pretrained(model_name_or_path,**model_args)
        tokenizer = MBartTokenizerFast.from_pretrained(model_name_or_path,**tokenizer_args)
    elif model_type == "gpt2":
        model = GPT2LMHeadModel.from_pretrained(model_name_or_path,**model_args)
        tokenizer = GPT2TokenizerFast.from_pretrained(model_name_or_path,**tokenizer_args)
    else:
        raise NotImplementedError
    return {"model" : model, "tokenizer" : tokenizer, "type" : model_type, "model_name_or_path" : model_name_or_path}
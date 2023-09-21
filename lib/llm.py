from langchain.llms.base import LLM

class DynamicLLM :
    llm: LLM
    prefix: str
        
    def __init__ (self, llm: LLM, prefix: str) :
        self.llm = llm 
        self.prefix = prefix
        
    def __call__ (self, text) -> str :
        text = self.prefix + text
        return self.llm(text)
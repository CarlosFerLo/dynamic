from .llm import DynamicLLM

class DynamicAgent() :
    dllm: DynamicLLM
    prompt_template: str 
    input_args: List[str]
    # TODO: add support for widgets, functions and special tags
    
    def _validate_prompt_template(self) -> bool :
        """ Returns true if the prompt template is valid and false otherwhise.
        
        Validation tests:
            - all the input args appear in the prompt template with the format "{name}"
            - all widget tags are placed and they appear in the head section
        
        """
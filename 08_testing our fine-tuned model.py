# Import the required modules
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate

# Setup your prompt template
template = """Question: {question}
Answer: Let's work this out in a step by step way to be sure we have the right answer."""
prompt = PromptTemplate.from_template(template)

# Add callback to support streaming the response
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# The number of layers to put on the GPU. The rest will be on the CPU. If you don't know how many layers there are, you can use -1 to move all to GPU.
n_gpu_layers = -1

# Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.  
n_batch = 512  

# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path="./models/*.gguf",
    n_gpu_layers=n_gpu_layers,
    n_batch=n_batch,
    temperature=0.5,
    max_tokens=100,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

# Chain the prompt template with the LlamaCpp model for processing
llm_chain = prompt | llm

# Allow user to input a custom question for the model to answer
custom_question = input("Enter your question: ")

# You can replace the custom question with any question of your choice
llm_chain.invoke({"question": custom_question})

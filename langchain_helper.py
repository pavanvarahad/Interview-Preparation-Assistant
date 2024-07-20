from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def generate_interview_preparation(topic,difficulty):
    llm = Ollama(model="qwen2:0.5b", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

    prompt_template_question = PromptTemplate(
        input_variables=['cuisine'],
        template="I am preparing for an interview in the topic of {topic} with {difficulty} difficulty. Suggest a single technical question be very precise and relevant to the topic while generating question. Strictly give only one question in text format without using any markdown. Generating only one question is mandatory"
    )
    question_chain = LLMChain(llm=llm, prompt=prompt_template_question,output_key="question")

    prompt_template_answer = PromptTemplate(
        input_variables=['question'],
        template="Please provide a short answer for {question}. Be very careful and give the most precise answer for the technical question from the topic {topic} and difficulty is {difficulty}.Strictly give the answer in simple text format without using any markdown"
    )
    answer_chain = LLMChain(llm=llm, prompt=prompt_template_answer,output_key="answer")

    # Create the SequentialChain
    chain = SequentialChain(
        chains=[question_chain, answer_chain],
        input_variables = ['topic','difficulty'],
        output_variables=['question', 'answer'],
    )

    response = chain({'topic': topic, 'difficulty': difficulty})

    return response
# Import necessary libraries
from datasets import load_dataset
import asyncio
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer("all-MiniLM-L6-v2")
async def load_kazqad_dataset():
    dataset = await asyncio.to_thread(load_dataset, "issai/kazqad", "kazqad")
    return dataset
def calculate_similarity(question_embedding, example_embedding):
    return util.cos_sim(question_embedding, example_embedding).item()
async def find_answer(question_input, threshold=0.6):
    dataset = await load_kazqad_dataset()
    question_embedding = model.encode(question_input, convert_to_tensor=True)
    
    for example in dataset["train"]:
        example_embedding = model.encode(example["question"], convert_to_tensor=True)
        similarity_score = calculate_similarity(question_embedding, example_embedding)
        if similarity_score >= threshold:
            output_text = f"Question: {example['question']}\n"
            output_text += f"Context: {example['context']}\n"
            output_text += f"Answer: {example['answers']['text'][0]}\n"
            return output_text

    return "NO FIND DATA"

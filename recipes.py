##########
## Magic Recipes
## Generate recipes from Youtube cooking videos
## 
## last updated: 01/2025
##########

# libraries
import logging
import azure.functions as func 
from youtube_transcript_api import YoutubeTranscripApi
import openai
import re

# API Keys
YOUTUBE_API_KEY = ""
openai.api_key = ""


def get_video_id(url):
    """ get video ID from Youtube URL """
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    if match: 
        return match.group(1)
    else: 
        return None 

def get_video_transcript(video_id):
    """ get video transcript from id """
    try:
        transcript = YoutubeTranscripApi.get_transcript(video_id, languages=["en"])
        return " ".join(item['text'] for item in transcript)
    except Exception as e:
        logging.error(f"Error fetching transcript: {e}")
        return None

def generate_recipe(transcript):
    """ generate recipe from transcript """
    prompt = f"""
    Extract a structured recipt from the following transcript of a cooking video. The recipe should include:
    - A title
    - A list of ingredients
    - step-by-step instructions

    Transcript:
    {transcript}
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=800,
        temperature=0.7
    )

    return response.choices[0].text.strip()


def main(req: func.HttpRequest) -> func.HttpResponse:
    """ Azure function to process Youtube video and return recipe"""
    logging.info("Processing request to extract recipe from video")

    # parse request
    try:
        req_body = req.get_json()
        video_url = req_body.get("video_url")
    except ValueError:
        return func.HttpResponse("Invalid JSON input.", status_code=400)
    
    if not video_url:
        return func.HttpResponse("Missing 'video_url' parameter.", status_code=400)
    
    # get video ID
    video_id = get_video_id(video_url)

    # get transcript
    transcript = get_video_transcript(video_id)

    # generate recipe
    recipe = generate_recipe(transcript)

    if not recipe:
        return func.HttpResponse("Failed to generate recipe.", status_code=500)
    
    return func.HttpResponse(recipe, status_code=200)
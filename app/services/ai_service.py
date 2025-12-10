import httpx
import base64
import random
import urllib.parse
from fastapi import HTTPException

# Configuration
# SWITCHING TO: Pollinations.ai (Direct Image Endpoint)
# This fixes the 301 Redirect errors by using the correct API subdomain.
BASE_URL = "https://image.pollinations.ai/prompt/"

class AIService:
    @staticmethod
    def generate_illustration(file_obj, style_preset: str = "watercolor"):
        """
        Generates an image using Pollinations.ai.
        """
        # 1. Prepare Prompt based on Style
        style_map = {
            "watercolor": "watercolor painting of a cute happy child, children's book illustration, soft strokes, vibrant, masterpiece, white background",
            "3d-render": "3d render of a cute happy child, pixar style, disney style, smooth textures, bright lighting, 4k, octane render",
            "line-art": "coloring book page of a cute happy child, black and white line art, clean lines, minimal, ink drawing, white background"
        }
        
        base_prompt = style_map.get(style_preset, style_map["watercolor"])
        
        # Add random seed
        seed = random.randint(1, 100000)
        
        # 2. Construct URL
        # Corrected URL format to avoid 301 Redirects
        encoded_prompt = urllib.parse.quote(base_prompt)
        url = f"{BASE_URL}{encoded_prompt}?width=768&height=768&seed={seed}&model=flux&nologo=true"

        print(f"Generating with Pollinations: {style_preset}")

        # 3. Fetch Image
        # Added follow_redirects=True to handle any edge case redirects gracefully
        with httpx.Client(timeout=60.0, follow_redirects=True) as client:
            try:
                response = client.get(url)
                
                if response.status_code == 200:
                    # Success!
                    image_bytes = response.content
                    base64_img = base64.b64encode(image_bytes).decode("utf-8")
                    return f"data:image/jpeg;base64,{base64_img}"
                else:
                    raise Exception(f"Pollinations Error {response.status_code}")

            except Exception as e:
                print(f"AI Service Error: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Generation Failed: {str(e)}")
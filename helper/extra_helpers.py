import asyncio
import edge_tts



class extraHelpers:
    def __init__(self):
        pass

    async def return_voice(self, gender: str, language: str) -> dict:
        voices = await edge_tts.VoicesManager.create()
        return await voices.find(Gender=gender, Language=language)
    
    async def generate_voice(self, text: str, voice: str, speed: int, pitch: int, volume: int):
        return await edge_tts.Communicate(text, voice, rate=speed, pitch=pitch, volume=volume)
    

if __name__ == "__main__":
    extraHelpers()

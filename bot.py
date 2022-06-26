from pyrogram import Client
import os

# Create a new Client
app = Client(
    "EpicBots",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)


async def main():
    async with app:
        # Get bot results for "hello" from the inline bot @vid
        bot_results = await app.get_inline_bot_results("vid", "hello")

        # Send the first result to your own chat (Saved Messages)
        await app.send_inline_bot_result(
            "me", bot_results.query_id,
            bot_results.results[0].id)


app.run(main())

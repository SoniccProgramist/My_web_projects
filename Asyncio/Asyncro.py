import asyncio
import datetime
import time

# async def perform_in_talk(task_id, duration):
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Task id: {task_id}: Start execution on {duration} sec.")
#     await asyncio.sleep(duration)
#     print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Task id: {task_id}: End performing.")
#     return f'Task_id: {task_id}'
#
# async def main_process():
#     print('with gather')
#     start_time = time.perf_counter()
#
#     result = await asyncio.gather(
#         perform_in_talk(1,2),
#         perform_in_talk(2,1),
#         perform_in_talk(3,4)
#     )
#
#     end_time = time.perf_counter()
#     print(f'Total execution time: {end_time - start_time}')
#
#     print(f'Result {result}')
#
# if __name__ == '__main__':
#     asyncio.run(main_process())

# import aiohttp
#
# base_url = "https://jsonplaceholder.typicode.com"
#
# async def send_api_request(session, request_type, resource_id):
#     url = f"{base_url}/{request_type}/{resource_id}"
#
#     try:
#         async with session.get(url) as response:
#             response.raise_for_status()
#             data = await response.json()
#             return {"type": request_type, "id":resource_id, "data": data}
#     except aiohttp.ClientError as e:
#         print(e)
#         return {"type": request_type, "id":resource_id, "data": "error"}
# async def main():
#
#     request_data = [
#         ("posts", 1),
#         ("comments", 5), # Отримати коментар 5
#         ("todos", 10),   # Отримати todo 10
#         ("users", 2),    # Отримати користувача 2
#         ("posts", 9999)  # Неіснуючий пост для тесту помилки
#     ]
#
#     async with aiohttp.ClientSession() as session:
#         tasks = [send_api_request(session, request_type, resource_id) for request_type, resource_id in request_data]
#         response = await asyncio.gather(*tasks)
#
#     for resp in response:
#         print(resp)
#
# asyncio.run(main())

# Створіть асинхронну функцію `get_post_and_comments(session, post_id)`,
# яка одночасно (конкурентно) отримує дані про пост та всі його коментарі з JSONPlaceholder.
# URL для поста: `https://jsonplaceholder.typicode.com/posts/{post_id}`
# URL для коментарів: `https://jsonplaceholder.typicode.com/posts/{post_id}/comments`
# Виведіть заголовок поста та кількість коментарів.


сfrom flask import Flask, request, jsonify
import time
import threading

app = Flask(__name__)

# Хранилище сообщений
messages = []
clients = []  # Список для хранения клиентов, ожидающих новых сообщений

# Функция для отправки сообщений всем клиентам
def notify_clients():
    while clients:
        client = clients.pop(0)
        client['event'].set()  # Активируем событие для ожидания сообщений


@app.route('/send', methods=['POST'])
def send_message():
    """Принимает новое сообщение от клиента"""
    data = request.json
    message = data.get("message")
    if message:
        messages.append(message)  # Добавляем сообщение в общий список
        notify_clients()  # Уведомляем ожидающих клиентов
        return jsonify({"status": "Message received"}), 200
    return jsonify({"error": "No message provided"}), 400


@app.route('/receive', methods=['GET'])
def receive_message():
	    """Ожидает новые сообщения с использованием long polling"""
    last_index = int(request.args.get("last_index", 0))

    if last_index < len(messages):
        # Если есть новые сообщения, сразу возвращаем их
        return jsonify({
            "new_messages": messages[last_index:],
            "last_index": len(messages)
        })

    # Если сообщений нет, создаем событие для ожидания
    event = threading.Event()
    clients.append({"event": event})

    # Ждем уведомления или тайм-аута (например, 30 секунд)
    event.wait(timeout=30)

    # Если появились новые сообщения
    if last_index < len(messages):
        return jsonify({
            "new_messages": messages[last_index:],
            "last_index": len(messages)
        })
    else:
        # Если по-прежнему нет новых сообщений, возвращаем пустой ответ
        return jsonify({"new_messages": [], "last_index": last_index})


if __name__ == '__main__':
    app.run(debug=True)

import requests
from config import TOKEN_BOT, CHAT_ID


def enviar_alerta_telegram(mensaje: str, token: str = TOKEN_BOT, chat_id: str = CHAT_ID) -> bool:
    """Envía un mensaje formateado en HTML a Telegram.

    Devuelve True si la petición tuvo código 200, False en caso contrario.
    """
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": mensaje,
        "parse_mode": "HTML",
        "disable_web_page_preview": False,
    }

    try:
        respuesta = requests.post(url, data=payload, timeout=10)
        if respuesta.status_code == 200:
            print("✅ Alerta enviada a Telegram con éxito.")
            return True
        else:
            print(f"❌ Error al enviar Telegram: {respuesta.text}")
            return False
    except Exception as e:
        print(f"❌ Fallo de conexión con Telegram: {e}")
        return False

import io

from google.cloud.speech import enums
from google.cloud import speech
from google.cloud.speech import types
from google.oauth2 import service_account
from pydub import AudioSegment


def transcribe_audio(audio_data: AudioSegment, language: str):
    """Transcribe the given audio file."""

    # Checking credentials
    service_account_info = {
      "type": "service_account",
      "project_id": "iron-handler-274614",
      "private_key_id": "58a6ece718a6e2786aaec280733c2e9bfb14bfc9",
      "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDfFwmXKg2QgbdZ\nY8Bgunw6X1CtqkbFnt95vu9Af51dHBqyLpDtpMQ5jO0TVLSmpMEAy/PntrK+z/wV\nl3xUcAoTZi0ufFkpz6i5cQ/r/4bbCpvbsaYVUMx9dxaLJqWRHn4Qd51iKI3kGzlT\n1zUU8oCUbOMb0N2P58GuPXLlZLEOQ17wOU3BX2nHqk4XGP8m7U+vmY5rSNnOSFj3\nBGPTKRa26LgcrwTC1e3hv18MR0+0ScKxotPgf9hdqZobtZvq698qRzWksqwDEaWv\nBTe6gBQqY7AxQyjCqvtzjTEvHkulDaECvrZ6fsUwHawZAiVjg8u0PY/Zt5yOzWpr\nJY1fVMeZAgMBAAECggEAAQnNsuluBTtoF3RRfmpfKa6eE5EmaQ7byzdSYAL+MVR1\nGR6gGAP6KoNnfl/dm8LeCj8BYAucdo2KS6P4GhJF9btYmxBWv6q0AU9AupVJFXM/\nBFcvxFVIub8mAonmuEDSU/VoaAPzks0nQDWCV1VAczfH06lLy050bF6pRLdRlUFY\nSkX5GFjZaGO8ouHbzanEjrBhdxbWAik0Q7d4gJdvR6IiXs78Kuxa5gFedz/+mPwQ\npSJI5Y5ULmw67C+OecaKvzahfrdqP/c1zK57qurwpD5U/1i+g7pcvltlqVjT/JqF\nOawwC05kxKu+fFYK9Vuur21DbUq3MmEcHGmro6AtVQKBgQD2++x57aPkgvXfE+oT\nkKELCtcKv2X84JdOtuEtRbs5gnKgZhrNhapIH8u/yYTvCUBle8iA9+Qxe01Lp7ZI\n6Aa11+EUgnLT0ekVSu/7e9eKuZ+0NJxU1Qxdi+PgMT38fElY6Erk4/IHoWz1fgQG\nLAY3v17cR7Go2CcnJ+mUG6IwXQKBgQDnO9KQD15vldVSZId8u+SwVcoNMffsu3p7\n7Y95tUSGIsuZtMN2R2aD5k0H5RD6shD8hl7n+/brWYRypT4WUdq7aynt1tZMsgXy\nVwfJt2CloPM7/owOAgcA2qWzmOVGUsYSUtKS0usAWyTrq/bi0o+BbsmuNsKC9Xv3\npJTxgrvwbQKBgDncEK0Lr95jk6f76VVGB4QnuPLqncDc+HVXQG8zq8WwOpw670KA\ncsDMuhWm5v58o1pi4jjcWdgBs7zqgDiaKqBE/5SnbrESttDnKks22urDy5cS0CDL\nfEcZ83tc7dGNaD1sxcbTY6rH9VeZeuXbQGWk7lsabJNKd/mjTwQEaT19AoGBAKNO\nl6ZQhGSQUGlxQFLyrE9xN1LcYHmb6qRNoc/WGoAVYO+8P3Nwd9FdvDeAKt6zFdYS\n3EJArCGJRkZlt5Sx2KYWyDUGTrE55YNCvehTj3lKU56iZq2Z9vI+eVp++CYTXXoh\nbkBtn7TPqiKbf7Cv/tPtt5hHalZtI1FBtkNfDnZ9AoGBALHdOdJJDixOU+zqVKBx\nf//H23xf8QajyCXD5yP21IXsG3KA1HTTTFtm44dMmwvx/LV9S6mB/7MCJRABSZO1\n9EJORYyFn570KjTuj3DbOqtq/onQ+qQ0I19atJ4agA9l0IHCnwcU1MHdY4RRnh91\n2w0KKxkMldCjJDPKaBhcRFCM\n-----END PRIVATE KEY-----\n",
      "client_email": "alinisarhaider@iron-handler-274614.iam.gserviceaccount.com",
      "client_id": "110744493393819760650",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://oauth2.googleapis.com/token",
      "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
      "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/alinisarhaider%40iron-handler-274614.iam.gserviceaccount.com"
    }
    # credentials = service_account.Credentials.from_service_account_file('account_credentials.json')
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    client = speech.SpeechClient(credentials=credentials)

    start = 0
    end = 60000
    step = 60000
    response_list: list = list()
    time_offset_list: list = list()

    while start < len(audio_data):
        if end < len(audio_data):
            trimmed_data = audio_data[start:end]
        else:
            trimmed_data = audio_data[start:]

        buf = io.BytesIO()
        trimmed_data.export(buf, format='flac')

        audio = types.RecognitionAudio(content=buf.getvalue())

        # Setting configurations
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
            language_code=language,
            audio_channel_count=audio_data.channels,
            enable_word_time_offsets=True)

        # Requesting Speech-to-text Google API
        response = client.recognize(config, audio)

        response_list.append(response)
        time_offset_list.append(int(start / 1000))
        start += step
        end += step

    return response_list, time_offset_list

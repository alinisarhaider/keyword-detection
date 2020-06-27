from flask import Flask, request, url_for, redirect, render_template, jsonify
from youtube_operations import get_audio_stream
from speech_to_text_api_operations import transcribe_audio
from transcription_operations import get_transcriptions
from detect_keywords import get_detections
from datetime import datetime, timedelta
import math


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/detect', methods=['POST'])
def detect():
    # form_values = [x for x in request.form.values()]
    # url, keywords = form_values[0], form_values[1].split(',')#.split(' ')
    # audio_segment_buffer = get_audio_stream(video_url=url)
    # response, time_offset = transcribe_audio(audio_data=audio_segment_buffer, language='en-US')
    # transcription, timestamps_list = get_transcriptions(response_list=response, time_offset_list=time_offset)
    # detections = get_detections(keywords=keywords, transcription=transcription, timestamps_list=timestamps_list)
    #
    # html_file = open('templates/output.html', 'w')
    # data = "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Detect Keywords</title><link href='https://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'><link href='https://fonts.googleapis.com/css?family=Arimo' rel='stylesheet' type='text/css'><link href='https://fonts.googleapis.com/css?family=Hind:300' rel='stylesheet' type='text/css'><link href='https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>"
    # data += "<link type='text/css' rel='stylesheet' href='{{ url_for("
    # data += '"static", filename="./style.css") }}'
    # data += "'>"
    # data += "</head><body><div><center><table border=1'><tr style='text-align:left'><th>Keyword</th><th>Occurrence time in video (Min:Sec)</th></tr>"
    #
    # for key, value in detections.items():
    #     if len(value) == 0:
    #         data += f"<tr><td>{key}</td><td> Not Found </td></tr>"
    #     elif len(value) == 1:
    #         d = datetime(1, 1, 1) + timedelta(seconds=math.ceil(value[0]))
    #         data += f"<tr><td>{key}</td><td>{d.minute}:{d.second}</td></tr>"
    #     else:
    #         data += f"<tr><td rowspan='{len(value)+1}'>{key}</td></tr>"
    #         for i in value:
    #             d = datetime(1, 1, 1) + timedelta(seconds=math.ceil(i))
    #             data += f"<tr><td>{d.minute}:{d.second}</td></tr>"
    #
    # data += "</table></center></div></body></html>"
    # html_file.write(data)
    # html_file.close()

    return render_template('output.html')


if __name__ == '__main__':
    app.run(debug=True)

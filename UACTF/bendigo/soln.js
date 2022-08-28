let numbers = ['5192446687125757', '5192446687125857', '5192446687125957', '5192446688125057', '5192446688125157', '5192446688125257', '5192446688125357', '5192446688125457', '5192446688125557', '5192446688125657', '5192446688125757', '5192446688125857', '5192446688125957', '5192446689125057', '5192446689125157', '5192446689125257', '5192446689125357', '5192446689125457', '5192446689125557', '5192446689125657', '5192446689125757', '5192446689125857', '5192446689125957']

import fetch from 'node-fetch';

for(let number of numbers){
    await new Promise(r => setTimeout(r, 5000));
    fetch("https://ctf.uactf.com.au/api/v1/challenges/attempt", {
    "headers": {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "csrf-token": "0370f0efb9389989ecd665d57052d19458a5cf73d62281561c9e445e3dbc036b",
    "sec-ch-ua": "\".Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "session=dbf81155-6948-4f7e-b274-c16dc2f12195.5UD7eUITYNpxsDhTwV0NOQFkwF0",
    "Referer": "https://ctf.uactf.com.au/challenges",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": "{\"challenge_id\":46,\"submission\":\"UACTF{"+number+"}\"}",
  "method": "POST"
}).then(res => res.text())
.then(text => console.log(number, text));
}
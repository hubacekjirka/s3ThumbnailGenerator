<h1 align="center">Welcome to S3 Lambda Thumbnail Generator 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/hubacekjirka/s3ThumbnailGenerator/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/hubacekjirka" target="_blank">
    <img alt="Twitter: hubacekjirka" src="https://img.shields.io/twitter/follow/hubacekjirka.svg?style=social" />
  </a>
</p>

> Takes advantage of a serverless architecture provided by AWS Lambda. When an image file is uploaded to the given S3 bucket, a lambda function gets triggered. It executes Python code that loads the file from the S3 bucket, creates a thumbnail using PIL library and saves the result back to the S3 bucket.

## Install
Prerequisity: AWS Account
```sh
npm install -g serverless

sls deploy -v
```

## Author

👤 **Jiri Hubacek**

* Twitter: [@hubacekjirka](https://twitter.com/hubacekjirka)
* Github: [@hubacekjirka](https://github.com/hubacekjirka)

## 🙏Credits
* kefranabg: [Readme generator](https://github.com/kefranabg/readme-md-generator)
* Stephane Maarek [Udemy Course](https://towardsdatascience.com/tensorflow-image-recognition-python-api-e35f7d412a70)
* Mark Needham: [Serverless and Python](https://realpython.com/twitter-bot-python-tweepy/)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Jiri Hubacek](https://github.com/hubacekjirka).<br />
This project is [MIT](https://github.com/hubacekjirka/s3ThumbnailGenerator/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
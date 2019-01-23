Last couple of days, I was looking for the answer for **Django** and **React** together. I have tried with **create-react-app** with django. I was succeed. But I wasn't happy. Because Every time I need to build react files and refresh the browser. Actually I just hate it. So, after doing some research on it, I found an awesome solution with webpack, babel, webpack-loader etc...

### Tools that I'm going use here
**NPM** is package manager for nodejs. Though it's for NodeJS, but it widely used in JavaScript community.

**Webpack** is bundle creator. It takes JSX, React, ES6 and all their dependencies to compile them for browser.  It also allow you to use loaders for various types of files like, CSS, Images etc.

**Webpack Bundle Tracker** is for getting information from Webpack and store them to  a JSON file to communicate with Django. Actually it's help Django to understand which bundle is latest.

**Babel Loader** is basically a transpiler that helps to compile ES6 (Actually JSX in this case) translate to regular JavaScript to browser support.

**Django Webpack Loader** is work with `webpack-stats.json` file. It read current bundle file and load with django server. Where **Webpack Bundle Tracker** is always updating the `webpack-stats.json` file with current updated bundle.

### Setup Code Base
**NOTE:** This project structure is not mandatory for you. You may setup your own as you like to. Just make sure that you configured correctly.

**Help:** All the star (*) indicate the directory and all the plus (+) indicate files.

	* DjangoReactTogether
		* api  (This is simple django app)
			+ __init__.py
			* migrations
				+ __init__.py
				+ .... (migrations files)
			+ models.py
			+ tests.py
			+ urls.py
			+ views.py
			+ ..... (all other files if necessary)
		* client  (Here will be all the frontend files)
			* bundles
				+ main.testbundle-hash.min.js /* Here will be bundles generated by webpack */
			* src
				+ App.js
				+ index.js
				+ tests.js
				+ /* Put all the frontend files inside src, I personally like directory srtucture for all the seperated files */
		* django_react  (Here will be django project files)
			+ __init__.py
			+ settings.py
			+ urls.py
			+ wsgi.py
		* templates
			+ index.html
		* node_modules
			+ // all the frontend packeges that are installed from npm.
		+ webpack.config.js
		+ package.json


**Let's start's with `webpack.config.js`**
Edit your webpack config file with the following,
```javascript
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    // the base directory (absolute path) for resolving the entry option
    context: __dirname,
    // your current directory. You don't have to specify the extension  now,
    // because you will specify extensions later in the `resolve` section
    entry: './client/src/index', 
    
    output: {
        // Where bundles will be stored
        path: path.resolve('./client/bundles/'), 
        filename: '[name]-[hash].js', 
    },
    
    plugins: [
        // tells webpack where to store data about your bundles. 
        new BundleTracker({filename: './webpack-stats.json'}), 
        // Just trying to make jquery available in every modules
        new webpack.ProvidePlugin({ 
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery'
        })
    ],
    
    module: {
        loaders: [
            // a regexp that tells webpack use the following loaders on all 
            // .js and .jsx files
            {
                test: /\.jsx?$/, 
                // we definitely don't want babel to transpile all the files in 
                // node_modules. That would take a long time.
                exclude: /node_modules/, 
                // use the babel loader 
                loader: 'babel-loader', 
                query: {
                    // specify that we will be dealing with React code
                    presets: ['react'] 
                }
            },
            // the next regex tells webpack to use style-loader and css-loader
            // (notice the chaining through the '!' syntax)
            // on all css files
            {
                test: /^(?!.*?\.module).*\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.module\.css$/,
                use: ['style-loader', {
                    loader: 'css-loader',
                    options: {
                        modules: true
                    }
                }]
            },
            {
                test: /\.png$/,
                use: 'url-loader?limit=100000'
            },
            {
                test: /\.jpg$/,
                use: 'file-loader'
            },
            {
                test: /\.png$/,
                use: 'url-loader?limit=100000'
            },
            {
                test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/,
                loader: 'url?limit=10000&mimetype=application/font-woff'
            },
            {
                test: /\.tff(\?v=\d+\.\d+\.\d+)?$/,
                loader: 'url-loader?limit=10000&mimetype=application/octet-stream'
            },
            {
                test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
                loader: 'file-loader'
            },
            {
                test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
                loader: 'url-loader?limit=10000&mimetype=image/svg+xml'
            },
        ]
    },
    
    resolve: {
        // tells webpack where to look for modules
        modules: ['node_modules'],
        // extensions that should be used to resolve modules
        extensions: ['*', '.js', '.jsx']
    }   
};
```
<br/>
Edit `package.json` and save with following codes,

```json
{
    "name": "django-react-together",
    "version": "1.0.0",
    "description": "Django and React Together",
    "main": "index.js",
    "scripts": {
        "dev": "webpack --watch",
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    "keywords": [
        "django",
        "django rest framework",
        "react",
        "webpack"
    ],
    "author": "Ashraful Islam",
    "license": "MIT",
    "devDependencies": {
        "babel-core": "^6.26.0",
        "babel-loader": "^7.1.2",
        "babel-preset-es2015": "^6.24.1",
        "babel-preset-react": "^6.24.1",
        "css-loader": "^0.28.7",
        "extract-text-webpack-plugin": "^3.0.2",
        "file-loader": "^1.1.5",
        "jquery": "^3.2.1",
        "react": "^16.2.0",
        "react-dom": "^16.2.0",
        "style-loader": "^0.19.0",
        "url-loader": "^0.6.2",
        "webpack": "^3.10.0",
        "webpack-bundle-tracker": "^0.2.0"
    },
    "dependencies": {}
}
```

##### It's time to do something with React
Put the following code on `src/index.js`

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
```

<br/>
Put the following code on `src/App.js`

```jsx
import React, { Component } from 'react';

class App extends Component {
  render() {
    return (
      {/* Write JSX Here... */}
    );
  }
}
export default App;
```
<br/>
**Frontend configuration is OK. Let's do with Django.**

Edit your `django_react/settings.py` and follow the instructions,
<br/>
* Add `webpack_loader` on installed apps.
* Paste the following code on `TEMPLATE` section.
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
				# DIRS should be configured properly
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'client')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**Static file Config**
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "client"),
]
```

**Django Webpack Loader Config**
```python
WEBPACK_LOADER = {
	'DEFAULT': {
		'BUNDLE_DIR_NAME': 'bundles/',
		'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
	}
}
```

**Open your `views.py` and place the snippet**
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

**Open `urls.py` and add the url**
```python
urlpatterns = [
	...
	path('', index, name='index-url'),
	...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

**Edit you `index.html`**
```
{% load render_bundle from webpack_loader %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django & React Together</title>
</head>
<body>
    <div id="root"></div>
    {% render_bundle 'main' %}
</body>
</html>
```
<br/>
**All Set!! Let's run the server...**
<br/>
Open two terminal/console window and run The follwing commands.

```bash
npm  install
npm run dev
# Switch another tab
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Follow your server address and keep going ...


#### Success
Finally you in the end of the page. I hope you will get a good taste of React & Django. Hope you'll like it. If I do any kind of mistake please don't feel shy to comment or send me an email.








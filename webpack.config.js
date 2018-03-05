const path = require('path');
const webpack = require('webpack');

const config = {
    resolve: {
        extensions: ['.coffee', '.js', '.sass'],
        modules: [ path.resolve( __dirname, 'node_modules' ) ]
    },
    entry: {
        'articlebox.bundle.js': ['babel-polyfill', './statics/apps/boot.dist.js']
    },
    output: {
        path: path.resolve(__dirname, 'statics/dist'),
        filename: '[name]',
        libraryTarget: 'var'
    },
    module: {
        rules: [
            { test: /\.html$/, use: 'raw-loader' },
            { test: /\.css$/,  use: ['style-loader', 'css-loader'] },
            {
                test: /\.sass$/,
                use: [{
                    loader: "style-loader" // creates style nodes from JS strings
                }, {
                    loader: "css-loader" // translates CSS into CommonJS
                }, {
                    loader: "sass-loader" // compiles Sass to CSS
                }]
            },
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['env']
                    }
                }
            },
            {
                test: /\.coffee$/,
                use: [ 'coffee-loader' ]
            },
            {
                test: /\.(png|jpg|jpeg|gif|svg|woff|woff2|ttf|eot)$/,
                loader: 'url-loader?limit=8192'
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            }
        ],
    },
    //plugins: [new webpack.ProvidePlugin({
    //    _: "lodash"
    //})]
};

module.exports = config;

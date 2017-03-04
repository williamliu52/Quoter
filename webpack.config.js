var path = require("path"),
    webpack = require("webpack"),
    ExtractTextPlugin = require("extract-text-webpack-plugin"),
    ManifestRevisionPlugin = require("manifest-revision-webpack-plugin")

var root = "./assets"

module.exports = {
    entry: {
        app_js: [
            root + "/scripts/index.js"
        ],
        main_css: [
            root + "/styles/index.css"
        ]
    },
    output: {
        path: "./public",
        publicPath: "/assets/",
        filename: "[name].[chunkhash].js",
        chunkFilename: "[id].[chunkhash].chunk"
    },
    resolve: {
        extensions: [".js", ".jsx", ".css"]
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                query: {
                    presets: ['es2015', 'react']
                }
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: "css-loader"
                })
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin({
            filename: "[name].[chunkhash].css"
        }),
        new ManifestRevisionPlugin('manifest.json', {
            rootAssetPath: root,
            ignorePaths: ["/styles", "/scripts", ".DS_Store"]
        }),
        new webpack.optimize.UglifyJsPlugin(),
        new webpack.DefinePlugin({
            "process.env": {
                NODE_ENV: '"production"'
            }
        })
    ]
}

let proxyHost = "https://api.twitter.com";

module.exports = {
    devServer: {
        host: "localhost",
        port: `5000`,
        // 代理链接配置
        proxy: {
            "/api": {
                target: proxyHost,
                changeOrigin: true,
                pathRewrite: {
                    "^/api": ""
                }
            }
        }
    },
    productionSourceMap: process.env.NODE_ENV === 'production' ? false : true,

}

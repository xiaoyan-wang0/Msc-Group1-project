// 其他第三方插件也可以追加到里面
import { JSDOM } from "jsdom"
const dom = new JSDOM()
global.document = dom.window.document
global.window = dom.window

const jquery = require('jquery')	
global.$ = jquery
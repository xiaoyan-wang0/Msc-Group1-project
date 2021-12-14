class ToolMethod {
    showToxicText(rate) {
        if (rate > 0.54) {
            return " Toxic";
        } else {
            return " Non Toxic";
        }
    }

    showToxicImg(rate) {
        if (rate > 0 && rate <= 0.54) {
            return require("@/assets/toxic-green.png");
        } else {
            return require("@/assets/toxic-red.png");
        }
    }

    showSentiemntText(rate) {
        if (rate < 0.5) {
            return " Negative";
        } else if (rate > 0.5 && rate < 1.5) {
            return " Positive";
        } else {
            return " Neutral";
        }
    }

    showSentiemntImg(rate) {
        if (rate > 0.4 && rate <= 0.6) {
            return "Neutral";
        } else if (rate > 0.6) {
            return "Positive";
        } else {
            return "Negative";
        }
    }

    changeToPercent(number) {
        return Number.parseInt(number * 100) + "%";
    }

    formatDate(string) {
        const date = new Date(string);
        return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
    }

    judgeBadWord(valuel) {
        //trim() 方法不会改变原始字符串 去掉首尾空白符
        this.contents = valuel.trim()
        var re = ''
        //正则过滤 模版字符串 \b 是一个整单词
        for (var i = 0; i < badWords.length; i++) {
            if (i == badWords.length - 1)
                re += `\\b${badWords[i]}\\b`
            else
                re += `\\b${badWords[i]}\\b` + "|"
        }
        var reg = new RegExp(re, "gi")
        this.contents = this.contents.replace(reg, '<font color="red">' + " *** " + '</font>')
        return this.contents

        // const value2 = badWords;
        // (value2 || []).map(function (item) {
        //     let reg = new RegExp(item, 'g');
        //     valuel = valuel.replace(reg, '<font color="red" >' + " *** " + '</font>');
        // });
        // return valuel;
    }

    judgeBadWordOther(valuel) {
        this.contents = valuel.trim()
        var re = ''
        //正则过滤 模版字符串 \b 是一个整单词
        for (var i = 0; i < badWords.length; i++) {
            if (i == badWords.length - 1)
                re += `\\b${badWords[i]}\\b`
            else
                re += `\\b${badWords[i]}\\b` + "|"
        }
        var reg = new RegExp(re, "gi")
        this.contents = this.contents.replace(reg, " *** ")
        return this.contents

        // const value2 = badWords;
        // (value2 || []).map(function (item) {
        //     let reg = new RegExp(item, 'g');
        //     valuel = valuel.replace(reg, " *** ");
        // });
        // return valuel;
    }

    //取出随机数, maxNum为 取出随机数的个数
    RandomNumBoth(arr, maxNum) {
        var numArr = [];
        //最大的循环次数
        var arrLength = arr.length;
        for (var i = 0; i < arrLength; i++) {
            //获取arr的长度
            var Rand = arr.length
            //取出随机数 
            var number = Math.floor(Math.random() * arr.length); //生成随机数num
            //往新建的数组里面传入数值
            numArr.push(arr[number]);
            //传入一个删除一个，避免重复
            arr.splice(number, 1);
            if (arr.length <= arrLength - maxNum) {
                return numArr;
            }
        }
    }

    // add more
}

const badWords = [
    '2g1c', '2 girls 1 cup', 'acrotomophilia', 'alabama hot pocket', 'alaskan pipeline', 'anal', 'damn', 'sh!t',
    'anilingus', 'anus', 'apeshit', 'arsehole', 'ass', 'asshole', 'assmunch', 'auto erotic', 'autoerotic',
    'babeland', 'baby batter', 'baby juice', 'ball gag', 'ball gravy', 'ball kicking', 'ball licking', 'ball sack',
    'ball sucking', 'bangbros', 'bareback', 'barely legal', 'barenaked', 'bastard', 'bastardo', 'bastinado', 'bbw', 'bdsm',
    'beaner', 'beaners', 'beaver cleaver', 'beaver lips', 'bestiality', 'big black', 'big breasts', 'big knockers', 'big tits',
    'bimbos', 'birdlock', 'bitch', 'bitches', 'black cock', 'blonde action', 'blonde on blonde action', 'blowjob', 'blow job', 'blow your load',
    'blue waffle', 'blumpkin', 'bollocks', 'bondage', 'boner', 'boob', 'boobs', 'booty call', 'brown showers', 'brunette action', 'bukkake', 'bulldyke',
    'bullet vibe', 'bullshit', 'bung hole', 'bunghole', 'busty', 'butt', 'buttcheeks', 'butthole', 'camel toe', 'camgirl', 'camslut', 'camwhore', 'carpet muncher',
    'carpetmuncher', 'chocolate rosebuds', 'circlejerk', 'cleveland steamer', 'clit', 'clitoris', 'clover clamps', 'clusterfuck', 'cock', 'cocks', 'coprolagnia',
    'coprophilia', 'cornhole', 'coon', 'coons', 'creampie', 'cum', 'cumming', 'cunnilingus', 'cunt', 'dafuq', 'dank', 'darkie', 'date rape', 'daterape',
    'deep throat', 'deepthroat', 'dendrophilia', 'dick', 'dork', 'dildo', 'dingleberry', 'dingleberries', 'dips hit', 'dirty pillows', 'dirty sanchez',
    'doggie style', 'doggiestyle', 'doggy style', 'doggystyle', 'dog style', 'dolcett', 'domination', 'dominatrix', 'dommes', 'donkey punch', 'double dong',
    'double penetration', 'douche', 'douchebag', 'dumbass', 'dp action', 'dry hump', 'dvda', 'eat my ass', 'ecchi', 'ejaculation', 'erotic', 'erotism', 'escort',
    'eunuch', 'fag', 'faggot', 'fecal', 'felch', 'fellatio', 'feltch', 'female squirting', 'femdom', 'figging', 'fingerbang', 'fingering', 'fisting', 'foot fetish',
    'footjob', 'frotting', 'fuck', 'fuck buttons', 'fuckin', 'fucking', 'fucktards', 'fudge packer', 'fudgepacker', 'futanari', 'gang bang', 'gay sex', 'genitals',
    'giant cock', 'girl on', 'girl on top', 'girls gone wild', 'goatcx', 'goatse', 'god damn', 'gokkun', 'golden shower', 'goodpoop', 'goo girl', 'goregasm',
    'grope', 'group sex', 'g-spot', 'guro', 'hand job', 'handjob', 'hard core', 'hardcore', 'hentai', 'hoe', 'homoerotic', 'honkey', 'hooker', 'hot carl',
    'hot chick', 'how to kill', 'how to murder', 'huge fat', 'humping', 'incest', 'intercourse', 'jack off', 'jail bait', 'jailbait', 'jelly donut', 'jerk off',
    'jigaboo', 'jiggaboo', 'jiggerboo', 'jizz', 'juggs', 'kike', 'kinbaku', 'kinkster', 'kinky', 'knobbing', 'leather restraint', 'leather straight jacket',
    'lemon party', 'lolita', 'lovemaking', 'make me come', 'male squirting', 'masturbate', 'menage a trois', 'milf', 'missionary position', 'motherfucker',
    'mound of venus', 'mr hands', 'muff diver', 'muffdiving', 'nambla', 'nawashi', 'negro', 'neonazi', 'nigga', 'nigger', 'nig nog', 'nimphomania', 'nipple',
    'nipples', 'nsfw images', 'nude', 'nudity', 'nympho', 'nymphomania', 'octopussy', 'omorashi', 'one cup two girls', 'one guy one jar', 'orgasm', 'orgy',
    'paedophile', 'paki', 'panties', 'panty', 'pedobear', 'pedophile', 'pegging', 'penis', 'phone sex', 'piece of shit', 'pissing', 'piss pig', 'pisspig',
    'playboy', 'pleasure chest', 'pole smoker', 'ponyplay', 'poof', 'poon', 'poontang', 'punany', 'poop chute', 'poopchute', 'porn', 'porno', 'pornography',
    'prince albert piercing', 'pthc', 'pubes', 'pussy', 'queaf', 'queef', 'quim', 'raghead', 'raging boner', 'rape', 'raping', 'rapist', 'rectum',
    'reverse cowgirl', 'rimjob', 'rimming', 'rosy palm', 'rosy palm and her 5 sisters', 'rusty trombone', 'sadism', 'santorum', 'scat', 'schlong',
    'scissoring', 'semen', 'sex', 'sexo', 'sexy', 'shaved beaver', 'shaved pussy', 'shemale', 'shibari', 'shit', 'shitblimp', 'shitty', 'shota',
    'shrimping', 'skeet', 'slanteye', 'slut', 's&m', 'smut', 'snatch', 'snowballing', 'sodomize', 'sodomy', 'spic', 'splooge', 'splooge moose',
    'spooge', 'spread legs', 'spunk', 'strap on', 'strapon', 'strappado', 'strip club', 'style doggy', 'suck', 'sucks', 'suicide girls', 'sultry women',
    'swastika', 'swinger', 'tainted love', 'taste my', 'tea bagging', 'threesome', 'throating', 'tied up', 'tight white', 'tit', 'tits', 'titties',
    'titty', 'tongue in a', 'topless', 'tosser', 'towelhead', 'tranny', 'tribadism', 'tub girl', 'tubgirl', 'tushy', 'twat', 'twink', 'twinkie',
    'two girls one cup', 'undressing', 'upskirt', 'urethra play', 'urophilia', 'vagina', 'venus mound', 'vibrator', 'violet wand', 'vorarephilia',
    'voyeur', 'vulva', 'wank', 'wetback', 'wet dream', 'whore', 'white power', 'wrapping men', 'wrinkled starfish', 'xx', 'xxx', 'yaoi', 'yellow showers',
    'yiffy', 'zoophilia', '__'
];


export default new ToolMethod();
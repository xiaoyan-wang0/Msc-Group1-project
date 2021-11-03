class ToolMethod {
    showToxicText(rate) {
        if (rate > 0 && rate <= 0.53) {
            return "Non toxic";
        } else if (rate > 0.53 && rate < 0.9) {
            return "Toxic";
        } else {
            return "Severe toxic";
        }
    }
    showToxicImg(rate) {
        if (rate > 0 && rate <= 0.53) {
            return "/img/toxic-green.31dbd2c6.png";
        } else if (rate > 0.53 && rate < 0.9) {
            return "/img/toxic-yellow.4f83d804.png";
        } else {
            return "/img/toxic-red.7e1e0c69.png";
        }
    }

    showSentiemntText(rate) {
        if (rate > 0.5) {
            return "Positive";
        } else {
            return "Negative";
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
        return Number(number * 100).toFixed(2) + "%";
    }

    formatDate(string) {
        const date = new Date(string);
        return date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
    }


    // add more
}

export default new ToolMethod();
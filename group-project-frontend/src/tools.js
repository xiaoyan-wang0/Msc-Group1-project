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

    showSentiemntText(rate) {
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
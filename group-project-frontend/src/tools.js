class ToolMethod {
    showToxicText(rate) {
        if (rate > 0 && rate <= 0.4) {
            return "No toxic";

        } else if (rate > 0.4 && rate < 0.7) {
            return "Middle toxic";

        } else {
            return "Real toxic";
        }
    }
    // add more
}

export default new ToolMethod();
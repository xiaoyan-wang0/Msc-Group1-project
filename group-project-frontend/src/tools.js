class ToolMethod {
    showToxicText(rate) {
        if (rate > 0 && rate <= 0.5) {
            return "Non toxic";

        } else if (rate > 0.5 && rate < 0.8) {
            return "Middle toxic";

        } else {
            return "Obsence toxic";
        }
    }
    // add more
}

export default new ToolMethod();
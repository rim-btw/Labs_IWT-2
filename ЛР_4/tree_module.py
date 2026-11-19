function task(value) {
    let encoded = '';
    let i = 0;
    
    while (i < value.length) {
        let count = 1;
        while (i + 1 < value.length && value[i] === value[i + 1]) {
            count++;
            i++;
        }
        encoded += value[i] + count;
        i++;
    }
    
    return {
        login: '1160509',
        encoded: encoded
    };
}
class SatisfactionChart extends Chart {
    constructor(ctx, data) {
        super(ctx, {
            type: 'pie',
            data: {
                labels: ['Muito Mau', 'Mau', 'Satisfaz', 'Bom', 'Muito Bom'],
                datasets: [{
                    data: data,
                    backgroundColor: [
                        'red',
                        'brown',
                        'yellow',
                        'cornflowerblue',
                        'lightgreen'
                    ]
                }]
            }
        });
    }
}


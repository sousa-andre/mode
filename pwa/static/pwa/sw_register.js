if ('serviceWorker' in navigator) {
    addEventListener('load', async ()=>{
        await navigator.serviceWorker.register('/static/pwa/sw.js')
            .catch(e => console.log(e));
    })
}

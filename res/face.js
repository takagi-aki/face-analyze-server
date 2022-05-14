let analyze = async (video, canvas, root, getimg) => {
    let context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    let dataURI = canvas.toDataURL("image/jpeg", 0.5);
    let dataBase64 = dataURI.split(",")[1];
    let body = JSON.stringify({ data: dataBase64 });
    let res = await fetch(`${root}face/emotion?getimg=${getimg}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: body
    });
    res = await res.blob();
    res = await res.text();
    return JSON.parse(res);
}

var face_analyze = (video, canvas, callback, root = './', gatimg = false) => {

    loop = async () => {
        let analyzed_info = await analyze(video, canvas, root, gatimg);
        callback(analyzed_info);
        setTimeout(()=>{loop()}, 10);
    };

    loop();
}

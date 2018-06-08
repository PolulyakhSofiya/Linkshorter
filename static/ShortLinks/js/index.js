function copyToClipboard(value, e) {
    let element = copyToClipboard.caller.arguments[0].srcElement;
    doBounce(element, 2, '10px', 4);

    let target = document.createElement("input");
    document.body.appendChild(target);
    target.value = value;
    target.select();
    document.execCommand("copy");
    target.remove();
}


function doBounce(element, times, distance, speed) {
    Velocity(element, { fontSize: 30,  }, 200).velocity({fontSize: '1em', marginLeft: 0}, {duration: 200});
}
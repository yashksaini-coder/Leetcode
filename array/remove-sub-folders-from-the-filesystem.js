
var removeSubfolders = function (folder) {
    folder.sort((a, b) => a.length - b.length)
    let set = new Set()
    primary: for (let dir of folder) {
        let dirArr = dir.split('/')
        let parDir = ''
        for (let i = 1; i < dirArr.length; i++) {
            parDir += `/${dirArr[i]}`
            if (set.has(parDir)) continue primary
        }
        set.add(parDir)
    }
    return Array.from(set)
};
const cheerio = require('cheerio');

function not_sub_list(_, elem) {
    while (elem?.parentNode?.tagName) {
        elem = elem.parentNode
        const tag = elem.tagName.toLowerCase()
        if (tag == 'ol' || tag == "header") return false
    }
    return true
}

function print_nice(obj, depth = 3) {
    util = require('util')
    console.log(util.inspect(obj, {
        colors: true,
        depth,
        compact: false,
    }))
}


function get_instruction_list(id, div) {
    id++
    const res = { id }
    for (const child of div.children) {
        if (child.type != 'tag') continue
        const tag = child?.tagName?.toLowerCase()
        switch (tag) {
            case undefined:
            case 'div':
                continue
            case 'ol':
                const lis = []
                for (let li of child.children) {
                    if (li.type != 'tag') continue
                    lis.push(get_instruction_list(lis.length, li))
                }
                res['steps'] = lis
                break
            case 'h4':
                res['title'] = $(child).text()
                break
            case 'p':
                res['sub_title'] = $(child).text()
                break
            default:
                console.log('unknown tag', tag)
        }
    }
    return res
}

function save_json(obj) {
    const fs = require('fs')
    fs.writeFileSync('data.json', JSON.stringify(obj, null, 4))
}

let $ = undefined

async function scrape(url) {
    const res = await fetch(url)
    const text = await res.text()
    $ = cheerio.load(text)
    const ols = $('ol').filter(not_sub_list).map((_, elem) => elem.parent)
    const parsed = ols.map(get_instruction_list).get()
    parsed.forEach(elem => elem.url = url)
    save_json(parsed)
}

const url = 'https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1542431.html'
scrape(url)
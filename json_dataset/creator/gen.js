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


function get_instruction_list(_, div) {
    const res = {}
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
                    lis.push(get_instruction_list(_, li))
                }
                res['steps'] = lis
                break
            case 'h4':
                res['title'] = $(child).html()
                break
            default:
                res['instruction'] = `${res['instruction'] ?? ''}<${tag}>${$(child).html()}</${tag}>`
                break
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
    parsed.forEach(elem => {
        elem.url = url
        elem.status = 'incomplete'
    })
    return parsed
}

async function scrapeMany(urls) {
    res = []
    for (const url of urls) {
        res.push(...await scrape(url))
    }
    save_json(res)
}

// const url = 'https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_161063246409.html'
// scrape(url)

const urls = [
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1553542323.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N950964.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1147232.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1171112.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1171354.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1173679.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1186284.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1186612.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1186943.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1187267.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1201405.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_3746921522.html",
    "https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_161677217185.html"
]

scrapeMany(urls)
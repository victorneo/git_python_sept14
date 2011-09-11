from bottle import route, run, template

@route('/nsylvia')
def nsylvia():
    return template('nsylvia/nsylvia.tpl')

@route('/davidlowjw')
def davidlowjw():
    return template('davidlowjw/davidlowjw.tpl')

@route('/arulkumaran')
def arulkumaran():
    return template('arulkumaran/arulkumaran.tpl')

@route('/clchan1')
def clchan1():
    return template('clchan1/clchan1.tpl')

@route('/eviltofu')
def eviltofu():
    return template('eviltofu/eviltofu.tpl')

@route('/fionnagoh')
def fionnagoh():
    return template('fionnagoh/fionnagoh.tpl')

@route('/guan0031')
def guan0031():
    return template('guan0031/guan0031.tpl')

@route('/joelchua')
def joelchua():
    return template('joelchua/joelchua.tpl')

@route('/joshuatj')
def joshuatj():
    return template('joshuatj/joshuatj.tpl')

@route('/l110003')
def l110003():
    return template('l110003/l110003.tpl')

@route('/meera')
def meera():
    return template('meera/meera.tpl')

@route('/mingofdlut')
def mingofdlut():
    return template('mingofdlut/mingofdlut.tpl')

@route('/minhquanit')
def minhquanit():
    return template('minhquanit/minhquanit.tpl')

@route('/mohanbelani')
def mohanbelani():
    return template('mohanbelani/mohanbelani.tpl')

@route('/n1103113j')
def n1103113j():
    return template('n1103113j/n1103113j.tpl')

@route('/nhkhai')
def nhkhai():
    return template('nhkhai/nhkhai.tpl')

@route('/nirmeshrahul')
def nirmeshrahul():
    return template('nirmeshrahul/nirmeshrahul.tpl')

@route('/pk')
def pk():
    return template('pk/pk.tpl')

@route('/pran0004')
def pran0004():
    return template('pran0004/pran0004.tpl')

@route('/pulkit1')
def pulkit1():
    return template('pulkit1/pulkit1.tpl')

@route('/raji')
def raji():
    return template('raji/raji.tpl')

@route('/shortfart007')
def shortfart007():
    return template('shortfart007/shortfart007.tpl')

@route('/simiwako')
def simiwako():
    return template('simiwako/simiwako.tpl')

@route('/srivathsan92')
def srivathsan92():
    return template('srivathsan92/srivathsan92.tpl')

@route('/srli1')
def srli1():
    return template('srli1/srli1.tpl')

@route('/tritamhoang')
def tritamhoang():
    return template('tritamhoang/tritamhoang.tpl')

@route('/vaib0001')
def vaib0001():
    return template('vaib0001/vaib0001.tpl')

@route('/wflim1')
def wflim1():
    return template('wflim1/wflim1.tpl')

@route('/zezore')
def zezore():
    return template('zezore/zezore.tpl')

@route('/zkria')
def zkria():
    return template('zkria/zkria.tpl')


run(host='localhost', port=8080, reloader=True)



import asyncio

@asyncio.coroutine
def handler_url_xxx(request):
    pass
    
url_param = request.match_info['key']
query_params = parse_qs(request.query_string)

text = render('template', data)
return web.Response(text.encode('utf-8'))

@get('/blog/{id}')
    def get_blog(id):
        pass
       
@get('/api/comments')
def api_comments(*, page = '1'):
    pass
    
def get(path):
    '''
    Define decorator @get('/path')
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator
    

class RequestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self._func = fn
        
        @asyncio.coroutine
        def __call__(self, request):
            kw = ...获取参数
            r = yield from self,_func(**kw)
            return r
            
def add_route(app, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ','.join(inspect.signature(fn).parameters.keys())))
    app.router.add_route(method, path, RequestHandler(app, fn))
    
    

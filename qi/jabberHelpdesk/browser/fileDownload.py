import mimetypes
import os.path
import base64
from Products.Five.browser import BrowserView
from ZPublisher.Iterators import IStreamIterator

class FileIterator(object):
    """ZPublisher iterator."""
    __implements__ = (IStreamIterator,)
    
    def __init__(self, input, streamsize=1<<16):
        self.input=input
        self.streamsize=streamsize
    
    def next(self):
        data = self.input.read(self.streamsize)
        if not data:
            raise StopIteration
        return data
    
    def __len__(self):
        cur_pos = self.input.tell()
        self.input.seek(0, 2)
        size = self.input.tell()
        self.input.seek(cur_pos, 0)
        
        return size

class FileDownloadView(BrowserView):
    """
    """
    
    def __call__(self):
        path = self.request.get('file',None)
        if not path:
            return ''
        path = base64.decodestring(path)
        filename = path.split('/')[-1]
        output = open(path,"rb")
        iterator=FileIterator(output)
        
        self.request.response.setHeader(
            'Content-Disposition',
            'attachment; filename=%s'%filename)
        self.request.response.setHeader("Content-Type", self.mimetype(path))
        self.request.response.setHeader('Content-Length', len(iterator))
        
        return iterator

    
    def mimetype(self,path):
        try:
            return mimetypes.types_map[os.path.splitext(path)[1]]
        except KeyError:
            return "application/octet-stream"

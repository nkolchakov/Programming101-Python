chapter_to_add = ''

class BookReader:
    def __init__(self, file_name):
        self._file_name = file_name

    def read_block_till(self,end):
        txt = self._file_name
        lines = []
        global chapter_to_add

        with open(txt) as data:
            while True:
                curr_line = next(data)
                if not curr_line.strip().startswith(end):
                    lines.append(curr_line)
                elif curr_line.strip() == '\n':
                    continue
                else:
                    lines.append(chapter_to_add)
                    chapter_to_add = curr_line.split('\n',1)[0]
                    res = lines
                    lines = []
                    yield res


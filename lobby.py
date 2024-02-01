from .table import Table
# lobby

def get_table(tid: int) -> Table:
    for t in tables:
        if t.tid == tid:
            return t
    return None

if __name__ == '__main__':
    tables = [Table(x) for x in range(10)]
import os
from angr import *

def main():
	project = angr.Project("./SMarT-solver", auto_load_libs=False)
	pp = project.factory.path_group()
	pp.explore(find=lambda path: 'Correct input!' in path.state.posix.dumps(1),avoid=lambda path: 'Sorry, that is not the correct input.' in path.state.posix.dumps(1))
	return pp.found[0].state.posix.dumps(0)

if __name__=='__main__':
	print(repr(main()))

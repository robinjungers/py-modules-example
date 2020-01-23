from ..common import common_fn
from ..module_other.file_other import Other

class A :
	def __init__( self ) :
		print( 'I am class A' )

		other = Other()

		common_fn()
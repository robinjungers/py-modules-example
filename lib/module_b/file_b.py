from ..common import common_fn
from ..module_other.file_other import Other

class B :
	def __init__( self ) :
		print( 'I am class B' )

		other = Other()

		common_fn()
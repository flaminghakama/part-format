# layoutFormats.py

#  Define the valid page formats
validPageFormats = {
	'1': 'half', 
	'1L': 'half', 
	'1R': 'half', 
	'2': 'half', 
	'2L': 'half', 
	'2R': 'half',
	'2X': 'full', 
	'3': 'half', 
	'3X': 'half', 
	'3XL': 'half', 
	'3XR': 'half', 
	'4': 'full',
	'4X': 'full',
	'5': 'half', 
	'5L': 'half', 
	'5R': 'half', 
	'5X': 'half',
	'5XL': 'half',
	'5XR': 'half',
	'6': 'half',
	'6L': 'half',
	'6R': 'half', 
	'6X': 'full',
	'7': 'half', 
	'7X': 'half',
	'7XL': 'half',
	'7XR': 'half',
	'8': 'full', 
	'8X': 'full',
	'9': 'half',
	'9L': 'half', 
	'9R': 'half',
	'9X': 'half', 
	'9XL': 'half',
	'9XR': 'half',
	'10': 'half', 
	'10L': 'half', 
	'10R': 'half', 
	'10X': 'full', 
	'11': 'half', 
	'11X': 'half', 
	'11XL': 'half',
	'11XR': 'half',
	'12': 'full',
	'12X': 'full'
}

pageFormats = {

	'1L': { 
		'full': [ None ],
		'half': { 'outside':1 'inside':None }
	}, 
	'1R': { 
		'full': [ None ], 
		'half': { 'outside':None 'inside':1 }
	}, 

	'2L': {
		'full': [ None ], 
		'half': { 'outside':1 'inside':2 }
	}, 
	'2R': {
		'full': [ None ],
		'half': { 'outside':2 'inside':1 }
	}, 

	'2X': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] } ],
		'half': None
	}, 

	'3': {
		'full': [ { 'outside':[0, 1], 'inside':[2, 3] } ],
		'half': None
	}, 

	'3XL': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] } ],
		'half': { 'outside':0 'inside':3 }
	}, 

	'3XR': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] } ],
		'half': { 'outside':3 'inside':0 }
	}, 

	'4': {
		'full': [ { 'outside':[4, 1], 'inside':[2, 3] } ],
		'half': None
	}, 

	'4X': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] } ],
		'half': None
	}, 

	'5L': {
		'full': [ { 'outside':[0, 1], 'inside':[2, 5] } ],
		'half': { 'outside':3 'inside':4 }
	}, 
	'5R': {
		'full': [ { 'outside':[0, 1], 'inside':[2, 5] } ],
		'half': { 'outside':4 'inside':3 }
	}, 

	'5XL': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] } ],
		'half': { 'outside':0 'inside':5 }
	}, 
	'5XR': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] } ],
		'half': { 'outside':5 'inside':0 }
	}, 

	'6L': {
		'full': [ { 'outside':[6, 1], 'inside':[2, 5] } ],
		'half': { 'outside':3 'inside':4 }
	}, 
	'6R': {
		'full': [ { 'outside':[6, 1], 'inside':[2, 5] } ],
		'half': { 'outside':4 'inside':3 }
	}, 
	'6X': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] } ],
		'half': None
	}, 

	'7': {
		'full': [ { 'outside':[0, 1], 'inside':[2, 7] },
		          { 'outside':[6, 3], 'inside':[4, 5] } ],
		'half': None
	}, 
	'7XL': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] } ],
		'half': { 'outside':0 'inside':7 }
	}, 
	'7XR': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] } ],
		'half': { 'outside':7 'inside':0 }
	}, 

	'8': {
		'full': [ { 'outside':[8, 1], 'inside':[2, 7] },
		          { 'outside':[6, 3], 'inside':[4, 5] } ],
		'half': None
	}, 
	'8X': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] },
				  { 'outside':[0, 0], 'inside':[7, 8] } ],
		'half': None
	}, 

	'9L': {
		'full': [ { 'outside':[0, 1], 'inside':[2, 9] },
		          { 'outside':[8, 3], 'inside':[4, 7] } ],
		'half': { 'outside':5 'inside':6 }
	}, 
	'9R': {
		'full': [ { 'outside':[0, 1], 'inside':[2, 9] },
		          { 'outside':[8, 3], 'inside':[4, 7] } ],
		'half': { 'outside':6 'inside':5 }
	}, 
	'9XL': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] },
				  { 'outside':[0, 0], 'inside':[7, 8] } ],
		'half': { 'outside':0 'inside':9 }
	}, 
	'9XR': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] },
				  { 'outside':[0, 0], 'inside':[7, 8] } ],
		'half': { 'outside':9 'inside':0 }
	}, 

	'10L': {
		'full': [ { 'outside':[10, 1], 'inside':[2, 9] },
		          { 'outside':[8, 3], 'inside':[4, 7] } ],
		'half': { 'outside':5 'inside':6 }
	}, 
	'10R': {
		'full': [ { 'outside':[10, 1], 'inside':[2, 9] },
		          { 'outside':[8, 3], 'inside':[4, 7] } ],
		'half': { 'outside':6 'inside':5 }
	}, 
	'10X': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] },
				  { 'outside':[0, 0], 'inside':[7, 8] },
				  { 'outside':[0, 0], 'inside':[9, 10] } ],
		'half': None
	}, 

	'11': {
		'full': [ { 'outside':[0, 1], 'inside':[2, 11] },
		          { 'outside':[10, 3], 'inside':[4, 9] },
		          { 'outside':[8, 5], 'inside':[6, 7] } ],
		'half': None
	}, 
	'11XL': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] },
				  { 'outside':[0, 0], 'inside':[7, 8] },
				  { 'outside':[0, 0], 'inside':[9, 10] } ],
		'half': { 'outside':0 'inside':11 }
	}, 
	'9XR': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] },
				  { 'outside':[0, 0], 'inside':[7, 8] },
				  { 'outside':[0, 0], 'inside':[9, 10] } ],
		'half': { 'outside':11 'inside':0 }
	}, 

	'12': {
		'full': [ { 'outside':[12, 1], 'inside':[2, 11] },
		          { 'outside':[10, 3], 'inside':[4, 9] },
		          { 'outside':[8, 5], 'inside':[6, 7] } ],
		'half': None
	},	
	'12X': {
		'full': [ { 'outside':[0, 0], 'inside':[1, 2] },
				  { 'outside':[0, 0], 'inside':[3, 4] },
				  { 'outside':[0, 0], 'inside':[5, 6] },
				  { 'outside':[0, 0], 'inside':[7, 8] },
				  { 'outside':[0, 0], 'inside':[9, 10] },
				  { 'outside':[0, 0], 'inside':[11, 12] } ],
		'half': None
	}, 
}

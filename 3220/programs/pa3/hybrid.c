/* Wesley Lewis
 * CPSC 3220
 * Project 3
 */

#include "hybrid.h"

char *bitmap_allocate() {

  //variables
  int i = 0;
  char *ptr = arena_head[0];
  long long int *currentAddress = 0;
  int shiftCount = 0;
  unsigned int binary = 1;

  //initialize "bit twiddler" to far left
  binary = binary << 31;
  
  //interate through bitmap and find an empty spot
  while (*ptr != 0) {
	
	  //go to next block and increment counter
	  ptr += ARENA_0_BLOCK_SIZE;
	  shiftCount++;

	  //go to next bitmap word if current is full
	  //and reset count
	  if (shiftCount == 32) { 
		  i++; 
		  shiftCount = 0;
	  }
  }

  //set current block to header_sig
  currentAddress = (long long int *) ptr;
  *currentAddress = HEADER_SIGNATURE;

  //shift binary by shiftCount and change bit in bitmap
  binary = binary >> shiftCount;
  bitmap[i] = bitmap[i] | binary;

  //decrement counter and return ptr 
  arena_count[0]--;
  return ptr + 8;
}


char *list_allocate (int size) {

  //variables
  char **ptr = (char **) arena_head[size];
  long long int *currentAddress = 0;

  //list is full, return
  if (ptr == NULL) return NULL;

  arena_head[size] = *ptr;

  currentAddress = (long long int *) ptr;
  *currentAddress = HEADER_SIGNATURE + size;

  arena_count[size]--;

  return (char *) (ptr) + 8;
}

char *allocate (int size) {
  if (size <= 0) {
    return NULL;
  }
  else if (size <= (arena_block_size[0] - 8)) {

    return bitmap_allocate();
  }
  else if (size <= (arena_block_size[1] - 8)) {

    return list_allocate (1);
  }
  else if (size <= (arena_block_size[2] - 8 )) {

    return list_allocate (2);
  }
  else {
    return NULL;
  }
}

void release (char *release_ptr) {
	char *ptr;
	long long unsigned int header, *header_ptr;

	if( (long long int) release_ptr & 0x7 ){
	   printf( "pointer not aligned on 8B boundary in release() function\n" );
		printf( "  => no action taken\n" );
		return;
   }
	if( ( release_ptr < min_address ) || ( release_ptr > max_address )  ){
		printf( "pointer out of range in release() function\n" );
		printf( "  => no action taken\n" );
		return;
	}
	ptr = release_ptr - 8;
	header_ptr = (long long unsigned int *) ptr;
	header = *header_ptr;
	if( ( header & 0xfffffff0 ) != HEADER_SIGNATURE ){
		printf( "header does not match in release() function\n" );
		printf( "  => no action taken\n" );
		return;
	}
}

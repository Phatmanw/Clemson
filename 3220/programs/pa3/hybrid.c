#include "hybrid.h"

char *bitmap_allocate() {
  char *p = arena_head[0];
  arena_head[0] += ARENA_0_BLOCK_SIZE;
  arena_count[0]--;
  
  return p + 8;
}


char *list_allocate (int size) {
  char *p = NULL;

  return p;
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

}

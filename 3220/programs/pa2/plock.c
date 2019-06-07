#include "plock.h"

plock_t *plock_create() {

	plock_t *ptr = malloc(sizeof(plock_t));
	ptr->value = FREE;
	pthread_mutex_init(&ptr->mlock, NULL);
	ptr->head = NULL;

	return ptr;
}

void plock_destory (plock_t *lock) {

}

void plock_enter (plock_t *lock, int priority) {

}

void plock_exit (plock_t *lock) { 

}

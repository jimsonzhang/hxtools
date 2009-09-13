/*
 *	Print architecture characteristics
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>

struct x16 {
	uint8_t a;
	uint16_t b;
};

struct x32 {
	uint8_t a;
	uint16_t b;
	uint32_t c;
};

struct x64 {
	uint8_t a;
	uint16_t b;
	uint32_t c;
	uint64_t d;
};

#define p(type) q(type, type)
#define q(type, vname) \
	extern int SIZEOF_##vname, ALIGNOF_##vname; \
	int SIZEOF_##vname = sizeof(type), ALIGNOF_##vname = __alignof__(type);
#define t(type) \
	printf("%14s  %7zu  %7zu\n", #type, sizeof(type), __alignof__(type))

p(char);
p(short);
p(int);
p(long);
q(long long, longlong);
p(float);
p(double);
q(long double, longdouble);
q(void *, voidptr);
q(void (*)(void), funcptr);
p(intptr_t);
p(wchar_t);
p(uint8_t);
p(uint16_t);
p(uint32_t);
p(uint64_t);
q(struct x16, x16);
q(struct x32, x32);
q(struct x64, x64);

#ifndef WITHOUT_MAIN
int main(void)
{
	printf("%14s  %7s  %7s\n", "TYPE", "SIZEOF", "ALIGNOF");
	t(char);
	t(short);
	t(int);
	t(long);
	t(long long);
	t(float);
	t(double);
	t(long double);
	t(void *);
	t(void (*)(void));
	t(intptr_t);
	t(wchar_t);
	t(uint8_t);
	t(uint16_t);
	t(uint32_t);
	t(uint64_t);
	t(struct x16);
	t(struct x32);
	t(struct x64);
	return EXIT_SUCCESS;
}
#endif
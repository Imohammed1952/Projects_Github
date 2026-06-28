#ifndef VEC3_H
#define VEC3_H

#include <cmath>
#include <iostream>

// vec3 class represents a 3D vector or point in space
class vec3 {
    public:
        // Member variables to store the x, y, and z components of the vector
        double e[3];

        // Constructors to initialize the vector, either to zero or to specific values
        vec3() : e{0,0,0} {}
        vec3(double e0, double e1, double e2) : e{e0, e1, e2} {}

        // Accessor methods to retrieve the x, y, and z components of the vector
        double x() const { return e[0]; };
        double y() const { return e[1]; };
        double z() const { return e[2]; };

        // Overloaded operators for vector arithmetic, including negation and indexing
        vec3 operator-() const { return vec3(-e[0], -e[1], -e[2]);  }
        double operator[](int i) const { return e[i]; }
        double& operator[](int i) {return e[i]; }
        
        // Overloaded operators for vector arithmetic, including addition, multiplication, and division
        vec3& operator+=(const vec3& v) {
            e[0] += v.e[0];
            e[1] += v.e[1];
            e[2] += v.e[2];
            return *this;
        };

        vec3& operator*=(double t) {
            e[0] *= t;
            e[1] *= t;
            e[2] *= t;
            return *this;
        };

        vec3& operator/=(double t) {
            return *this *= 1/t;
        };

        // Method to return the length (magnitude) of the vector
        double length() const {
            return std::sqrt(length_squared());
        };
        
        // Method to compute the length (magnitude) of the vector 
        double length_squared() const {
            return e[0]*e[0] + e[1]*e[1] + e[2]*e[2];
        };

};

// Type aliases for vec3 to represent points in 3D space
using point3 = vec3;

// Vector Utility Functions

inline std::ostream& operator<<(std::ostream& out, const vec3& v) {
    return out << v.e[0] << ' ' << v.e[1] << ' ' << v.e[2];
}

inline vec3 operator+(const vec3& u, const vec3& v) {
    return vec3(u.e[0] + v.e[0], u.e[1] + v.e[1], u.e[2] + v.e[2]);
};

inline vec3 operator-(const vec3& u, const vec3& v) {
    return vec3(u.e[0] - v.e[0], u.e[1] - v.e[1], u.e[2] - v.e[2]);
};

inline vec3 operator*(const vec3& u, const vec3& v) {
    return vec3(u.e[0] * v.e[0], u.e[1] * v.e[1], u.e[2] * v.e[2]);
};

inline vec3 operator*(double t, const vec3& v) {
    return vec3(t*v.e[0], t*v.e[1], t*v.e[2]);
};

inline vec3 operator*(const vec3& v, double t) {
    return t * v;
};

inline vec3 operator/(vec3 v, double t) {
    return (1/t) * v;
};

inline double dot(const vec3& u, const vec3& v) {
    return u.e[0] * v.e[0]
           + u.e[1] * v.e[1]
           + u.e[2] * v.e[2];
};

inline vec3 cross(const vec3& u, const vec3& v) {
    return vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1],
                u.e[2] * v.e[0] - u.e[0] * v.e[2],
                u.e[0] * v.e[1] - u.e[1] * v.e[0]);
};

inline vec3 unit_vector(vec3 v) {
    return v / v.length();
};
#endif
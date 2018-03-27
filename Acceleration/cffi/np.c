int cnt = 0;
void add(float *in1, float *in2, float *out, int width, int height){
    for(int y = 0; y < height; ++y){
        for(int x = 0; x < width; ++x, ++in1, ++in2, ++out){
            *out = *in1 + *in2;
        }
    }
    cnt++;
}
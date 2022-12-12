
public class NNRunner {

	public static void main(String[] args) {
		/*double[][] x = {{1.0,2.0,3.0,2.5}, {2.0,5.0,-1.0,2.0},{-1.5,2.7,3.3,-0.8}};
		
		neuralLayer layer1 = new neuralLayer(4,5);
		double[][] output1 = layer1.forwardSoftMax(x);
		neuralLayer layer2 = new neuralLayer(5,2);
		double[][] output2 = layer2.forwardSoftMax(output1);
		for(int i = 0; i < output2.length; i++) {
			for(int j = 0; j < output2[i].length; j++) {
				System.out.print(output2[i][j] + " , ");
			}
			System.out.println("");
		}*/
		
		ReadData data = new ReadData();
		neuralLayer layer1 = new neuralLayer(3,3);
		 double[][] w = { {0.1, 0.3, 0.4},
                 {0.2, 0.2, 0.3},
                 {0.3, 0.7, 0.9}};
		layer1.setWeights(w);
		double[][] output = layer1.forwardReLU(data.inputs);
		for(int i = 0; i < output.length; i++) {
			for(int j = 0; j < output[i].length; j++) {
				System.out.print(output[i][j] + " , ");
			}
			System.out.println("");
		}
		System.out.println("");
		
		
		neuralLayer layer2 = new neuralLayer(3,3);
		double[][] w2 = { {0.2, 0.3, 0.6},
                {0.3, 0.5, 0.4},
                {0.5, 0.7, 0.8}};
		layer2.setWeights(w2);
		double[][] output2 = layer2.forwardSigmoid(output);
		for(int i = 0; i < output2.length; i++) {
			for(int j = 0; j < output2[i].length; j++) {
				System.out.print(output2[i][j] + " , ");
			}
			System.out.println("");
		}
		System.out.println("");
		
		
		neuralLayer layer3 = new neuralLayer(3,3);
		double[][] w3 = { {0.1, 0.3, 0.5},
                {0.4, 0.7, 0.2},
                {0.8, 0.2, 0.9}};
		layer3.setWeights(w3);
		double[][] output3 = layer3.forwardSoftMax(output2);
		
		for(int i = 0; i < output3.length; i++) {
			double sum = 0;
			for(int j = 0; j < output3[i].length; j++) {
				System.out.print(output3[i][j] + " , ");
				sum += output3[i][j];
			}
			System.out.print(" SUM: " + sum);
			System.out.println("");
		}
		System.out.println("");
		double[] loss = layer3.loss(data.label, output3);
		for(int i = 0; i < loss.length; i++) {
			System.out.print(loss[i] + " ,");
		}
		

	}

}
